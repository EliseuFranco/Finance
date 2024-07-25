function screen_Changed() {
    const sideMenu = document.getElementById("side_menu");
    const closed = document.getElementById("closed");

    if (window.innerWidth >= 668) {
        sideMenu.style.display = "block";
        sideMenu.style.width = "100%";
        closed.style.display = "none";
    } else {
        sideMenu.style.display = "none";
        closed.style.display = "block";
    }
}

function show_Menu() {
    const sideMenu = document.getElementById("side_menu");
    if (sideMenu.style.display === "none") {
        sideMenu.style.display = "block";
        sideMenu.style.width = "200px";
    } else {
        sideMenu.style.display = "none";
    }
}

screen_Changed();

function open_Edit(){
    window.location.href = "../finance/templates/index.html";
}