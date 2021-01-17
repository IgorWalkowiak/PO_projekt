const deliveryRadios = document.querySelectorAll(".delivery-radio");
const addressForm = document.querySelectorAll("#address")[0];
const addressInput = document.querySelectorAll(".address-input");

function showIfNotPickupInPerson() {
  if (this.checked && this.defaultValue !== "pickup-in-person") {
    addressForm.classList.add("address-form-active");
    for (let i = 0; i < addressInput.length - 1; i++) {
      addressInput[i].required = true;
    }
  } else {
    addressForm.classList.remove("address-form-active");
    for (let i = 0; i < addressInput.length - 1; i++) {
      addressInput[i].required = false;
    }
  }
}

deliveryRadios.forEach((radio) => {
  radio.addEventListener("change", showIfNotPickupInPerson);
});
