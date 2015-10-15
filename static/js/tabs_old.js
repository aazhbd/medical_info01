window.onload=function() {
    // var navitem = $("#tabHeader_1");
    var navitem = $("#currentTab").val();
    //this adds click event to tabs
    var tabs = $("#tabContainer li");
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].onclick=displayPage;
    }
    $("#tabHeader_" + navitem).click();
}

// on click of one of tabs
function displayPage() {
  var current = this.parentNode.getAttribute("data-current");
  //remove class of activetabheader and hide old contents
  $("#tabHeader_" + current).removeAttr("class");
  var ident = this.id.split("_")[1];
  //add class of activetabheader to new active tab and show contents
  this.setAttribute("class","tabActiveHeader");
  var url = $("#tabID_" + ident).val();
  $("#tabscontent").load(url);
  this.parentNode.setAttribute("data-current",ident);
}
