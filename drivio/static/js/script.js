let crs = document.querySelector("#cursor");
let blur = document.querySelector("#cursor-blur");
let footer = document.querySelector(".footer");
const btn = document.querySelector(".full-rounded");
const btn_a = document.querySelector("#our-a");
const btn_f = document.querySelector("#our-f");
const btn_i = document.querySelector("#our-i");
const btn_c = document.querySelector(".connect");
const btn_o = document.querySelector("#owner");
const btn_d = document.querySelector("#driver");
const btn_start = document.querySelector("#start");

// btn_start.addEventListener("click", () => {
//   window.location.href = "login";
// });
// btn_a.addEventListener("click", () => {
//   window.location.href = "#card1";
// });
// btn_f.addEventListener("click", () => {
//   window.location.href = "#card2";
// });
// btn_o.addEventListener("click", () => {
//   window.location.href = "{% url 'owner'%}";
// });
// btn_d.addEventListener("click", () => {
//   window.location.href = "{% driver %}";
// });

document.addEventListener("mousemove", function (delts) {
  crs.style.left = delts.x + 20 + "px";
  crs.style.top = delts.y + 20 + "px";
  blur.style.left = delts.x - 150 + "px";
  blur.style.top = delts.y - 150 + "px";
});
footer.addEventListener("mouseenter", (e) => {
  // console.log(crs);
  // console.log(blur);

  console.log("Footer Entered");
});
function disableEffects() {
  if (crs) crs.style.display = "none"; // or add a class that hides the element
  if (blur) blur.style.display = "none"; // or add a class that removes the blur effect
}

// Function to enable crs and blur
function enableEffects() {
  if (crs) crs.style.display = ""; // or remove the class that hides the element
  if (blur) blur.style.display = ""; // or remove the class that removes the blur effect
}

footer.addEventListener("mouseenter", (e) => {
  console.log("Footer Entered");
  disableEffects();
});

footer.addEventListener("mouseleave", (e) => {
  console.log("Footer Left");
  enableEffects();
});
function navAnimation() {
  let nav = document.querySelector(".nav-part2");
  nav.addEventListener("mouseenter", function () {
    // gsap.to("#nav-bottom", {
    //   height: "12vh",
    // });

    let tl = gsap.timeline();
    tl.to("#nav-bottom", {
      height: "12vh",
      // backgroundColor: "black",
    });
    tl.to(".nav-part2 h5", {
      display: "block",
      // opacity: "100%",
    });
    tl.to(".nav-part2 h5 span", {
      y: 0,
      // duration: 0.4,
      stagger: {
        amount: 0.2,
      },
    });
  });
  nav.addEventListener("mouseleave", function () {
    let tl = gsap.timeline();

    tl.to(".nav-part2 h5 span", {
      y: 25,
      // duration: 0.4,
      stagger: {
        amount: 0.2,
      },
    });
    tl.to(".nav-part2 h5", {
      display: "none",
      duration: 0.1,
    });
    tl.to("#nav-bottom", {
      height: 0,
      duration: 0.2,
    });
  });
}
navAnimation();
gsap.to("#nav", {
  backgroundColor: "#000",
  height: "110px",
  duration: 0.5,
  scrollTrigger: {
    trigger: "#nav",
    scroller: "body",
    markers: false,
    start: "top -10%",
    end: "top -11%",
    scrub: 1,
  },
});
gsap.to("#main", {
  backgroundColor: "#000",
  duration: 0.5,
  scrollTrigger: {
    trigger: "#main",
    scroller: "body",
    markers: false,
    start: "top -20%",
    end: "top -75%",
    scrub: 2,
  },
});
gsap.from("#about-us img,#about-us-in", {
  y: 60,
  opacity: 0,
  duration: 1,
  stagger: 0.3,
  scrollTrigger: {
    trigger: "#about-us",
    scroller: "body",
    // markers: true,
    start: "top 70%",
    end: "top 60%",
    scrub: 2,
  },
});
// gsap.from(".card", {
//   scale: 0.9,
//   opacity: 0,
//   duration: 0.5,
//   stagger: 0.1,
//   scrollTrigger: {
//     trigger: ".card",
//     scroller: "body",
//     // markers: true,
//     start: "top 70%",
//     end: "top 65%",
//     scrub: 1,
//   },
// });
gsap.from("#colon1", {
  y: -70,
  x: -70,
  scrollTrigger: {
    trigger: "#colon1",
    scroller: "body",
    // markers: true,
    start: "top 55%",
    end: "top 40%",
    scrub: 4,
  },
});
gsap.from("#colon2", {
  y: 70,
  x: 70,
  scrollTrigger: {
    trigger: "#colon1",
    // markers: true,
    scroller: "body",
    start: "top 55%",
    end: "top 44%",
    scrub: 4,
  },
});
gsap.from("#page4 h1", {
  y: 30,
  scrollTrigger: {
    trigger: "#page4 h1",
    // markers: true,
    scroller: "body",
    start: "top 75%",
    end: "top 70%",
    scrub: 2,
  },
});
