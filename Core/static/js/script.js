var prevScrollPos = window.scrollY;
window.onscroll = function() {
  var currentScrollPos = window.scrollY;
  if (prevScrollPos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "100px";
    document.getElementById("navbar").style.color = "red";
  }
  prevScrollPos = currentScrollPos;
};

window.onscroll = function() {
  var footer = document.getElementById("footer");
  var scrollPosition = window.innerHeight + window.pageYOffset;
  var bodyHeight = document.body.offsetHeight;

  if (scrollPosition >= bodyHeight) {
    footer.style.display = "block";
  } else {
    footer.style.display = "none";
  }
};
