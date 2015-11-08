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
            otherwise({
                redirectTo: '/'
            });
        }
    ]); 

    drake.controller('MainController', ["$firebaseObject","Auth","$location", function($firebaseObject, Auth, $location){
        var main = this;
        
        main.client = {};
        main.loggedin = false;
        var clientRef;
        
        Auth.$onAuth(function(authData) {
            if(authData){
                clientRef = new Firebase("https://flywithdrake.firebaseio.com/users/" + authData.auth.uid);
                main.client = $firebaseObject(clientRef);
                main.client.$loaded(function(){
                    main.client[authData.auth.uid] = authData;
                    main.client.$save()
                });
                main.loggedin = true;
                $location.path('/home')
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
                $location.path('/home')
            }
        }
        
        main.logout = function(){
            Auth.$unauth();
            main.loggedin = false;
        };
    
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