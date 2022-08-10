//nav bar starts
hamburger = document.querySelector(".hamburger");
    hamburger.onclick = function () {
        navBar = document.querySelector(".nav-bar");
        navBar.classList.toggle("active");
    }
//navbar ends

//home starts
$(".testimonial_slider_area").owlCarousel({
                autoplay: true,
                slideSpeed: 3000,
                items: 3,
                nav: true,
                navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
                margin: 30,
                dots: false,
                responsive: {
                    320: {
                        items: 1
                    },
                    767: {
                        items: 2
                    },
                    600: {
                        items: 3
                    },
                    1000: {
                        items: 4
                    }
                }
            });
//home ends

//BOOTSTRAP JAVASCRIPT BEGINS
src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
crossorigin="anonymous"
//BOOTSTRAP JAVASCRIPT ENDS