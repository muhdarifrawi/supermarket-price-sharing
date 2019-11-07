/*global $*/

$("#left").hover(
    function(){
      $(this).css("opacity", "1");
      $(this).css("cursor","pointer");
    },
    function(){
        $(this).css("opacity","0.8");
    }
    
    );

$("#left").click(
    function(){
        window.location="/submit";
    }
    
    );

   
$("#right").hover(
    function(){
        $(this).css("opacity","1");
        $(this).css("cursor","pointer");
    },
    function(){
        $(this).css("opacity","0.8");
    }
    
    );
    
$("#right").click(
    function(){
        window.location="/table";
    }
    
    );