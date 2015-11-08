(function(){
    
    'use strict';

    var drake = angular.module('drake', [
        'ngRoute',
        'auth',
        'ui.bootstrap',
        'firebase'
    ]);
        
    drake.config(['$routeProvider','$locationProvider',
        function($routeProvider,$locationProvider) {
            $locationProvider.html5Mode(true).hashPrefix('!');
            $routeProvider.
            when('/login', {
                templateUrl: 'login.html'
            }).            
            when('/home', {
                templateUrl: 'home.html'
            }).
            when('/404', {
                templateUrl: '404.html'
            }).
            when('/recommendations', {
                templateUrl: 'rec.html'
            }).
            when('/item/:x', {
                templateUrl: 'detail.html'
            }).
            otherwise({
                redirectTo: '/'
            });
        }
    ]); 

    drake.controller('MainController', ["$firebaseObject","Auth","$location", "$firebaseArray", function($firebaseObject, Auth, $location, $firebaseArray){
        var main = this;
        var selectedFlight;
        
        var trips = [{'dest': 'Los Angeles, CA ', 'origin': 'JFK', 'price': '670.70', 'date': '2015-11-11'}, {'dest': 'Liberia, Costa Rica ', 'origin': 'JFK', 'price': '1268.76', 'date': '2015-11-15'}, {'dest': 'Grenada, Grenada', 'origin': 'JFK', 'price': '1085.29', 'date': '2015-11-22'}, {'dest': 'Curacao, Netherlands Antilles ', 'origin': 'JFK', 'price': '680.13', 'date': '2015-11-14'}, {'dest': 'Nassau, Bahamas - Paradise Island ', 'origin': 'JFK', 'price': '3137.18', 'date': '2015-11-21'}, {'dest': 'Tampa, FL ', 'origin': 'JFK', 'price': '834.31', 'date': '2015-11-22'}, {'dest': 'Bermuda, Bermuda ', 'origin': 'JFK', 'price': '1066.75', 'date': '2015-11-25'}, {'dest': 'West Palm Beach, FL ', 'origin': 'JFK', 'price': '1014.37', 'date': '2015-11-25'}, {'dest': 'Montego Bay, Jamaica ', 'origin': 'MCO', 'price': '441.75', 'date': '2015-11-22'}, {'dest': 'Aruba, Aruba ', 'origin': 'JFK', 'price': '1618.00', 'date': '2015-11-22'}, {'dest': 'Cancun, Mexico ', 'origin': 'FLL', 'price': '327.60', 'date': '2015-11-15'}, {'dest': 'La Romana, Dominican Republic ', 'origin': 'JFK', 'price': '961.15', 'date': '2015-11-25'}, {'dest': 'Puerto Plata, Dominican Republic ', 'origin': 'JFK', 'price': '1243.36', 'date': '2015-11-13'}, {'dest': 'Fort Lauderdale, FL ', 'origin': 'JFK', 'price': '1058.87', 'date': '2015-11-18'}, {'dest': 'Los Angeles, CA ', 'origin': 'JFK', 'price': '670.70', 'date': '2015-11-13'}, {'dest': 'Providenciales, Turks and Caicos Islands ', 'origin': 'JFK', 'price': '2342.93', 'date': '2015-11-12'}, {'dest': 'Santo Domingo, Dominican Republic - Las Americas ', 'origin': 'JFK', 'price': '538.59', 'date': '2015-11-11'}, {'dest': 'Bridgetown, Barbados ', 'origin': 'JFK', 'price': '834.33', 'date': '2015-11-25'}, {'dest': 'St. Lucia, St. Lucia ', 'origin': 'JFK', 'price': '947.38', 'date': '2015-11-16'}, {'dest': 'Fort Myers, FL ', 'origin': 'JFK', 'price': '445.81', 'date': '2015-11-18'}, {'dest': 'San Juan, Puerto Rico ', 'origin': 'JFK', 'price': '514.81', 'date': '2015-11-18'}, {'dest': 'New Orleans, LA ', 'origin': 'JFK', 'price': '844.49', 'date': '2015-11-21'}, {'dest': 'Orlando, FL - International ', 'origin': 'JFK', 'price': '692.93', 'date': '2015-11-22'}, {'dest': 'Grand Cayman, Cayman Islands ', 'origin': 'JFK', 'price': '743.41', 'date': '2015-11-12'}, {'dest': 'San Diego, CA ', 'origin': 'JFK', 'price': '730.12', 'date': '2015-11-20'}, {'dest': 'Las Vegas, NV ', 'origin': 'JFK', 'price': '574.26', 'date': '2015-11-21'}, {'dest': 'Samaná El Catey', 'origin': 'JFK', 'price': '1049.85', 'date': '2015-11-25'}, {'dest': 'New York, NY - Kennedy ', 'origin': 'BOS', 'price': '523.66', 'date': '2015-11-18'}, {'dest': 'San Francisco, CA ', 'origin': 'JFK', 'price': '959.60', 'date': '2015-11-13'}, {'dest': 'Charleston, SC ', 'origin': 'JFK', 'price': '1101.24', 'date': '2015-11-14'}, {'dest': 'Punta Cana, Dominican Republic', 'origin': 'FLL', 'price': '1159.83', 'date': '2015-11-18'}]
        
        main.findIndex = function(n){
            for(var i = 0; i<=30; i++){                
                if (n == trips[i].dest)
                    return i;
            }
        }
        
        function shuffle(array) {
          var currentIndex = array.length, temporaryValue, randomIndex ;

          // While there remain elements to shuffle...
          while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
          }

          return array;
        }
        
        main.client = {};
        main.loggedin = false;
        var clientRef;
        var randomizedFlights = []
        
        var flightRef = new Firebase("https://flywithdrake.firebaseio.com/flights/");
        main.flights = $firebaseArray(flightRef);
        main.flights.$loaded().then(function(){
            main.randomizedFlights = main.flights.slice(0);
            main.randomizedFlights = shuffle(main.randomizedFlights);
            console.log(main.randomizedFlights);
            console.log(main.flights);
        })
        
        Auth.$onAuth(function(authData) {
            if(authData){
                clientRef = new Firebase("https://flywithdrake.firebaseio.com/users/" + authData.auth.uid);
                main.client = $firebaseObject(clientRef);
                main.client.$loaded(function(){
                    main.client[authData.auth.uid] = authData;
                    main.client.$save()
                });
                main.loggedin = true;
                $location.path('/home');
            }
            main.authData = authData;
        });
        
        main.login = function(){
            if (!main.loggedin){
                Auth.$authWithOAuthPopup("facebook").then(function(authData) {
                    console.log(authData);
                    main.loggedin = true;
                    $location.path('/home')
                 }).catch(function(error) {
                    alert('There was an error with your login :(');
                });
            }else{
                console.log("login function was triggered while main.loggedin was false");
                $location.path('/home');
            }
        }
        
        main.logout = function(){
            Auth.$unauth();
            main.loggedin = false;
        };
        
        main.goto = function(x){
            $location.path('/item/'+x);
            main.s = x;
        }
        
        main.gotorec = function(){
            $location.path('/recommendations');
        }
                
        main.gotohome = function(){
            $location.path('/home');
        }
    
    }]);


})();


(function(){
    'use strict';
    
    var auth = angular.module('auth', ['firebase']);
    
    auth.factory('Auth',["$firebaseAuth", function($firebaseAuth){
        var authRef = new Firebase("https://flywithdrake.firebaseio.com");
        return $firebaseAuth(authRef);
    }]);
})();