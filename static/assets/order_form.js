const deliveryRadios = document.querySelectorAll(".delivery-radio");
const addressForm = document.querySelectorAll("#address")[0];

function showIfNotPickupInPerson() {
  if (this.checked && this.defaultValue !== "pickup-in-person") {
    addressForm.classList.add("address-form-active");
  } else {
    addressForm.classList.remove("address-form-active");
  }
}

deliveryRadios.forEach((radio) => {
  radio.addEventListener("change", showIfNotPickupInPerson);
});
