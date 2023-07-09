$(document).ready(function () {
  // Toggle mobile menu
  $('#menu-toggle-mobile').change(function () {
    var mobileMenu = $('#mobile-menu');
    if ($(this).is(':checked')) {
      mobileMenu.removeClass('hidden');
    } else {
      mobileMenu.addClass('hidden');
    }
  });

  // Close mobile menu on outside click
  $(document).click(function (e) {
    var target = $(e.target);
    var mobileMenu = $('#mobile-menu');
    var menuToggle = $('#menu-toggle-mobile');
    if (!target.is(mobileMenu) && !target.is(menuToggle) && mobileMenu.has(e.target).length === 0) {
      mobileMenu.addClass('hidden');
      menuToggle.prop('checked', false);
    }
  });
});