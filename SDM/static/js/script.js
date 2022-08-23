//nav bar starts
// hamburger = document.querySelector(".hamburger");
//     hamburger.onclick = function () {
//         navBar = document.querySelector(".nav-bar");
//         navBar.classList.toggle("active");
//     }
// //navbar ends

//sidebar starts
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");


closeBtn.addEventListener("click", () => {
        sidebar.classList.toggle("open");
        menuBtnChange(); //calling the function(optional)
    });

    // following are the code to change sidebar button(optional)
function menuBtnChange() {
        if (sidebar.classList.contains("open")) {
            closeBtn.classList.replace("bx-menu", "bx-menu-alt-right"); //replacing the iocns class
        } else {
            closeBtn.classList.replace("bx-menu-alt-right", "bx-menu"); //replacing the iocns class
        }
    }
//sidebar ends

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
