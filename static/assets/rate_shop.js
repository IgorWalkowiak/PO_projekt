$("#rate-shop").click(function () {
  const rating = $("#rate-shop-form input[type='radio']:checked").val();
  const text = $("textarea#rate-shop-text").val() || null;
  console.log(rating, text);
  alert("Dziękujemy za ocenę sklepu!");

  $.ajax({
    type: "POST",
    url: "/rate",
    data: {
      rate: rating,
      text: text,
    },
  });

  $(this).prop("disabled", true);
});
