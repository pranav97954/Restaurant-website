let shop = document.getElementById('shop');
let drink = document.getElementById('drink');

let basket = JSON.parse(localStorage.getItem("data")) || [];

function myonclickfunction()
{
        var x = document.getElementById("menu");

        if(x.style.display== "block")
        {
            x.style.display = "none";
        }
        else{
            x.style.display = "block";
        }

}

let getMenuItem = () =>{
    return (shop.innerHTML = menuitem.map((x) => {
        return `
        <div class="cart-item">
            <img  width="100px" src="${x.img}" alt="">
            <div class="title-price-x">
               <h4 class="title-price">
                 <p>${x.name}</p>
                 <p class="cart-item-price" >Rs ${x.price}</p>
               </h4>
            </div>
        </div>
        `;
    }).join(""));
};
getMenuItem();

let getDrinkItem = () =>{
    return (drink.innerHTML = drinkitem.map((x) => {
        return `
        <div class="cart-item">
            <img  width="100px" src="${x.img}" alt="">
            <div class="title-price-x">
               <h4 class="title-price">
                 <p>${x.name}</p>
                 <p class="cart-item-price" >Rs ${x.price}</p>
               </h4>
            </div>
        </div>
        `;
    }).join(""));
};
getDrinkItem();