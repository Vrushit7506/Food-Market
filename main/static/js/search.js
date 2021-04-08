var searchFood = document.getElementById("searchFood");
var pannel = document.getElementById("searched");

all_dishes = JSON.parse(all_dishes.replace(/&quot;/g, '"'));
// console.log(all_dishes);

searchFood.addEventListener("keyup", (e) => {
  pannel.innerHTML = "";
  searchedEle = all_dishes.filter((dish) =>
    dish["name"].toLowerCase().includes(e.target.value.toLowerCase())
  );

  if (searchedEle.length > 0) {
    searchedEle.map((item) => {
      pannel.innerHTML += `
        <a href="/menu/${item["cuisine"]}" >
					<li>
					<div class="fooditem">
						<div class="foodPhoto">
							<img src="../../static/images/Cuisines/${item["cuisine"]}.jpg" alt="" />
						</div>
						<div class="content">
							<div class="like"></div>
							<div class="icon">
								<h4> ₹ ${item["price"]}</h4>
							</div>
							<section>
								<div class="bg-item"></div>
								<div class="bg-text">
									<div class="stars"></div>
									<h2>${item["name"]}</h2>
									<h4>${item["cuisine"]}</h4>
								</div>
							</section>
						</div>
					</div>
				</li>
        </a>`;
    });
  } else if (searchedEle.length == 0) {
    pannel.innerHTML += `
						<h4 style = "color: white; font-weight: 300; text-align: center;">
							No Dish Found
						</h4>
						`;
  }
});

function searchItem() {
  let newestLi = document.getElementById("newestLi");
  let topHorizontal = document.getElementById("topHorizontal");

  var liEl = document.getElementsByClassName("liEl");
  for (let i = 0; i < liEl.length; i++) {
    liEl[i].classList.remove("active");
  }

  var searchClass = document.getElementsByClassName("Searched");
  if (searchClass.length == 0) {
    let li = document.createElement("li");
    li.classList.add("liEl");
    li.classList.add("Searched");
    li.classList.add("active");
    li.innerHTML = "Searched";
    li.onclick = function () {
      changePannel(this, "searched");
    };
    topHorizontal.insertBefore(li, newestLi);
  }
  searchClass[0].classList.add("active");
  var pannel1 = document.getElementsByClassName("pannel");
  var pannel = document.getElementById("searched");

  for (let i = 0; i < pannel1.length; i++) {
    pannel1[i].style.display = "none";
  }

  pannel.style.display = "block";
}

let submit = document.getElementById("submit");
submit.addEventListener("click", searchItem);
