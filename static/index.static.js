/*global $*/

$("#left").hover(
    function(){
      $(this).css("opacity", "1");  
    },
    function(){
        $(this).css("opacity","0.8");
    }
    
    );

   
$("#right").hover(
    function(){
        $(this).css("opacity","1");
    },
    function(){
        $(this).css("opacity","0.8");
    }
    
    );