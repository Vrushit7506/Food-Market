function footerSwitch(clickedTab, mainId) {
  var footerTabs = document.getElementsByClassName("footerTab");
  for (let i = 0; i < footerTabs.length; i++) {
    footerTabs[i].classList.remove("active");
  }
  clickedTab.classList.add("active");

  var mainSections = document.getElementsByClassName("mainSection");
  for (let i = 0; i < mainSections.length; i++) {
    mainSections[i].classList.remove("active");
  }
  var viewSection = document.getElementById(mainId);
  viewSection.classList.add("active");
}

function exploreSwitch(clickedTab, mainId) {
  var exploreTabs = document.getElementsByClassName("exploreTab");

  for (let i = 0; i < exploreTabs.length; i++) {
    exploreTabs[i].classList.remove("active");
  }

  clickedTab.classList.add("active");

  var c = document.getElementsByClassName("cusines");
  for (let i = 0; i < c.length; i++) {
    c[i].classList.remove("active");
  }
  var v = document.getElementById(mainId);
  v.classList.add("active");
}

$(".user_chat").attr("data-attr", "Mr. Green");

function ChatOpen() {
  var chatArea = document.getElementsByClassName("chattingArea");
  chatArea[0].scrollTop = chatArea[0].scrollHeight;
}

function changePannel(liElement, pannel) {
  var liEl = document.getElementsByClassName("liEl");
  for (let i = 0; i < liEl.length; i++) {
    liEl[i].classList.remove("active");
  }

  liElement.classList.add("active");

  var pannel1 = document.getElementsByClassName("pannel");
  var pannel = document.getElementById(pannel);

  for (let i = 0; i < pannel1.length; i++) {
    pannel1[i].style.display = "none";
  }

  pannel.style.display = "block";
}
