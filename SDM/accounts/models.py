from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.urls import reverse

# custom manager for user


class MyAccountManager(BaseUserManager):
    # custom account manager because we want to use email instead of username
    use_in_migrations = True

    def _create_user(self, email, password, name, **extra_fields):
        """
        Create and save a user with the given email,name and password.
        """
        if not email:
            raise ValueError("Email must be set")
        # if not password:
        #     raise ValueError("Password is not provided")

        email = self.normalize_email(email)

        user = self.model(email=email, name=name, ** extra_fields)

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, ** extra_fields)

    def create_superuser(self, email, password, ** extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, ** extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    # Create Roles for the users
    class Roles(models.TextChoices):
        SCHOOL = 'SCHOOL', 'School'
        GUARDIAN = 'GUARDIAN', 'Guardian'

    # The default role for a user
    base_role = Roles.GUARDIAN

    # what type of user are we?
    role = models.CharField(max_length=50,
                            choices=Roles.choices, null=True, default=base_role)

    email = models.EmailField(db_index=True, verbose_name='email',
                              max_length=60, unique=True, null=True)
    name = models.CharField(max_length=255, verbose_name='name')

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name='last joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    avatar = models.ImageField(
        max_length=255, null=True, default='Ellipse 1.svg')

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'email': self.email})

    # sets the base role when object is created from user
    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        if self.name:
            self.name = self.name.title()
        return super().save(*args, **kwargs)


# for when you query Guardian. returns only objects with role = user.Roles.GUARDIAN
class GuardianManager(MyAccountManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.GUARDIAN)


# for when you query School. returns only objects with role = user.Roles.School
class SchoolManager(MyAccountManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.SCHOOL)


# Guardian group of User
class Guardian(User):
    base_role = User.Roles.GUARDIAN
    objects = GuardianManager()
    # guardianmore = GuardianMore()

    # makes GuardianMore an attribute of Guardian.more
    @property
    def profile(self):
        return self.guardianprofile

    # does not create a new table. gotten from the user table
    class Meta:
        proxy = True


# more fields assicited to Guardian model
class GuardianProfile(models.Model):
    user = models.OneToOneField(Guardian, on_delete=models.CASCADE)
    phone = models.IntegerField()


class GuardianChild(models.Model):
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    relationship = models.CharField(max_length=30)

    # name to display on the admin panel
    class Meta:
        verbose_name = 'Guardian Child'
        verbose_name_plural = 'Guardian Children'

# School group of User


class School(User):
    base_role = User.Roles.SCHOOL
    objects = SchoolManager()

    # makes SchoolMore an attribute of School.more
    @property
    def profile(self):
        return self.schoolprofile

    # does not create a new table. gotten from the user table
    class Meta:
        proxy = True

# School.objects.all()
# School.name
# School.email
# School.schoolprofile.phone
# School.schoolprofile.alt_phone
# School.schoolprofile.address
# more fields assicited to School model


class SchoolProfile(models.Model):
    user = models.OneToOneField(School, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)
    alt_phone = models.IntegerField(null=True)
    lga_code = models.CharField(max_length=3)
    state_code = models.CharField(max_length=3)
    address = models.CharField(max_length=255, null=True)
    cac = models.CharField(max_length=255)  # file field
    moe = models.CharField(max_length=255)  # file field

    class Meta:
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Profiles'


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    class_of_withdrawal = models.CharField(max_length=20)
    date_of_withdrawal = models.DateTimeField(null=True)
    debt_incured = models.DecimalField(max_digits=11, decimal_places=2)
    interest_incured = models.DecimalField(max_digits=50, decimal_places=2)

    avatar = models.ImageField(
        max_length=255, null=True, default='Ellipse 1.svg')


# Create School
# school = School.objects.create(enter fields)

# Add extra fields to School
# Schoolprofile.objects.create(user=school_instance, extra_fields...)

# Add Student
# student = Student.objects.create(school=school_instance, extra_fields...)

# Create Guardian
# guardian_name = school.objects.create(enter fields)

# Add extra fields to Guardian
# GuardianProfile.objects.create(user=guardian_instance, extra_fields...)

# Add GuardianChild
# child = GuardianChild.objects.create(guardian=guardian_instance, extra_fields...)

# search for students in a school
# Student.objects.filter(school=school_instance)

# search for childern of a guardian
# GuardianChild.objects.filter(guardian=guardian_instance)
