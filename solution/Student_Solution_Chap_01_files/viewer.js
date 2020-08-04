 $(function() {
            
var fixadent = $("#fixadent"), pos = fixadent.offset();
$(window).scroll(function() {
  
if($(this).scrollTop() > (pos.top + 10) && fixadent.css('position') == 'static') { fixadent.addClass('fixed'); }
else if($(this).scrollTop() <= pos.top && fixadent.hasClass('fixed')){ fixadent.removeClass('fixed'); }
})
});