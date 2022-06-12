function get_quote(){
const options = {
    method: 'GET',
    headers: {
		'X-RapidAPI-Key': '4585c1a6a8msh57e19c7c3ad0432p199ee6jsn9e7f84f03c48',
		'X-RapidAPI-Host': 'inspiring-quotes.p.rapidapi.com'
    }
};

fetch('https://inspiring-quotes.p.rapidapi.com/random?author=Albert', options)
    .then(response => response.json())
    .then(data => {

        document.getElementById('result').innerHTML = String(data.quote);
        }
       );

}


function get_weather(){

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '4585c1a6a8msh57e19c7c3ad0432p199ee6jsn9e7f84f03c48',
		'X-RapidAPI-Host': 'bestweather.p.rapidapi.com'
	}
};

fetch('https://bestweather.p.rapidapi.com/weather/38.736946,-9.142685/today?unitGroup=metric', options)
	.then(response => response.json())
	.then(data=> {
	    const weather = data;
	    document.getElementById('Descricao').innerHTML =String (weather.description)
        document.getElementById('temperatura').innerHTML = "Temperature : " + String (weather.currentConditions.temp) + "ºC"
        document.getElementById('Humidity').innerHTML = "Humidity: " + String (weather.currentConditions.humidity)
        document.getElementById('precip').innerHTML = "precipitation: " + String (weather.currentConditions.precip)
        document.getElementById('sunrise').innerHTML = "The sun rises at : " + String (weather.currentConditions.sunrise)
        document.getElementById('sunset').innerHTML = "The sun sets at : " + String (weather.currentConditions.sunset)


	});
}
function get_dice(){
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '4585c1a6a8msh57e19c7c3ad0432p199ee6jsn9e7f84f03c48',
		'X-RapidAPI-Host': 'roll-dice1.p.rapidapi.com'
	}
};

fetch('https://roll-dice1.p.rapidapi.com/rollDice', options)
	.then(response => response.json())
    .then(data => {
	    const dice = data;
        document.getElementById('dice').innerHTML = String(dice.data.Dice);
        document.getElementById('talk').innerHTML = String(dice.data.talk);

        }
       );

}




