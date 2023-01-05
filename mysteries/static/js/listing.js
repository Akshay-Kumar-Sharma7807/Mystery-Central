let pricing = document.querySelector("#pricing");
let auctionInput = document.querySelector("#auction-input");
let price = document.querySelector("#price");

console.log(pricing)
if (pricing.value == "auction") {
    price.classList.add("hidden")
}
else {
    auctionInput.classList.add("hidden")
}
pricing.onchange = () => {
    console.log(pricing.value)
    if (pricing.value == "auction") {
        auctionInput.classList.remove('hidden')
        price.classList.add("hidden")
    }
    else if (pricing.value == 'buyitnow') {
        auctionInput.classList.add("hidden");
        price.classList.remove("hidden")
    }
}