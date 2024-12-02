document.addEventListener('DOMContentLoaded', function() {
    const checkInInput = document.getElementById('check-in');
    const checkOutInput = document.getElementById('check-out');
    const totalDaysElement = document.getElementById('total-days');
    const hotelCards = document.querySelectorAll('.hotel-card');

    function updateTotalDays() {
        const checkInDate = new Date(checkInInput.value);
        const checkOutDate = new Date(checkOutInput.value);

        if (checkInDate && checkOutDate && checkOutDate > checkInDate) {
            const timeDiff = checkOutDate.getTime() - checkInDate.getTime();
            const nightsDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
            totalDaysElement.textContent = Total stay: ${nightsDiff} night${nightsDiff !== 1 ? 's' : ''};
            updateHotelPrices(nightsDiff);
        } else {
            totalDaysElement.textContent = '';
            resetHotelPrices();
        }
    }

    function updateHotelPrices(nights) {
        hotelCards.forEach(card => {
            const basePrice = parseInt(card.dataset.basePrice);
            const totalPrice = basePrice * nights;
            const priceElement = card.querySelector('.price');
            const totalPriceElement = card.querySelector('.total-price');

            priceElement.textContent = €${basePrice} per night;
            totalPriceElement.textContent = Total for ${nights} night${nights !== 1 ? 's' : ''}: €${totalPrice};
        });
    }

    function resetHotelPrices() {
        hotelCards.forEach(card => {
            const basePrice = card.dataset.basePrice;
            const priceElement = card.querySelector('.price');
            const totalPriceElement = card.querySelector('.total-price');

            priceElement.textContent = €${basePrice} per night;
            totalPriceElement.textContent = '';
        });
    }

    checkInInput.addEventListener('change', updateTotalDays);
    checkOutInput.addEventListener('change', updateTotalDays);
});