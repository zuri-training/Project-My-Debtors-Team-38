from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    # Create Roles for the users
    class Roles(models.TextChoices):
        SCHOOL = 'SCHOOL', 'School'
        GUARDIAN = 'GUARDIAN', 'Guardian'

    # The default role for a user
    base_role = Roles.GUARDIAN

    # what type of user are we?
    role = models.CharField(max_length=50,
                            choices=Roles.choices, default=base_role)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    # sets the base role when object is created from user
    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        return super().save(*args, **kwargs)

# for when you query Guardian. returns only objects with role = user.Roles.GUARDIAN


class GuardianManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.GUARDIAN)


# for when you query School. returns only objects with role = user.Roles.School
class SchoolManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.SCHOOL)


# more fields assicited to Guardian model
class GuardianMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(blank=False, max_length=255)
    m_name = models.CharField(blank=False, max_length=255)
    l_name = models.CharField(blank=False, max_length=255)
    phone = models.IntegerField()


# Guardian group of User
class Guardian(User):
    base_role = User.Roles.GUARDIAN
    objects = GuardianManager()
    # guardianmore = GuardianMore()

    # makes GuardianMore an attribute of Guardian.more
    @property
    def more(self):
        return self.guardianmore

    # does not create a new table. gotten from the user table
    class Meta:
        proxy = True


class GuardianChild(models.Model):
    guardian = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255)
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    relationship = models.CharField(max_length=30)


# more fields assicited to School model
class SchoolMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=255)
    phone = models.IntegerField()
    alt_phone = models.IntegerField()
    lga_code = models.CharField(max_length=3)
    state_code = models.CharField(max_length=3)
    cac = models.CharField(max_length=255)
    moe = models.CharField(max_length=255)
    # updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    school = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255)
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    class_of_withdrawal = models.CharField(max_length=20)
    date_of_withdrawal = models.DateTimeField(null=True)


# School group of User
class School(User):
    base_role = User.Roles.SCHOOL
    objects = SchoolManager()

    # makes SchoolMore an attribute of School.more
    @property
    def more(self):
        return self.schoolmore

    # does not create a new table. gotten from the user table
    class Meta:
        proxy = True


# Create School
# school = school.objects.create(enter fields)

# Add extra fields to School
# SchoolMore.objects.create(user=school_instance, extra_fields...)

# Add Student
# student = Student.objects.create(user=school_instance, extra_fields...)

# Create Guardian
# guardian_name = school.objects.create(enter fields)

# Add extra fields to Guardian
# GuardianMore.objects.create(user=guardian_instance, extra_fields...)

# Add GuardianChild
# child = GuardianChild.objects.create(user=guardian_instance, extra_fields...)

# search for students in a school
# Student.objects.filter(school=school_instance)

# search for childern of a guardian
# GuardianChild.objects.filter(guardian=guardian_instance)
