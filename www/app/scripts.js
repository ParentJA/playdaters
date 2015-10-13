(function (window, angular, undefined) {

  "use strict";

  function HttpConfig($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
  }

  function UiRouterConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state("user", {
        url: "/user",
        template: "<div ui-view></div>",
        resolve: {},
        abstract: true
      });

    //Default state...
    $urlRouterProvider.otherwise("/");
  }

  function UiRunner($rootScope, $state) {
    $rootScope.$state = $state;
  }

  function MainController($scope, $state, accountsService) {
    $scope.getUser = function getUser() {
      return accountsService.getUser();
    };

    $scope.hasUser = function hasUser() {
      return accountsService.hasUser();
    };

    $scope.logOut = function logOut() {
      accountsService.logOut().then(function () {
        $state.go("home");
      });
    };
  }

  angular.module("app", ["ngCookies", "ui.router"])
    .constant("BASE_URL", "/api/v1/")
    .config(["$httpProvider", HttpConfig])
    .config(["$stateProvider", "$urlRouterProvider", UiRouterConfig])
    .run(["$rootScope", "$state", UiRunner])
    .controller("MainController", ["$scope", "$state", "accountsService", MainController]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function AccountsRouterConfig($stateProvider) {
    $stateProvider
      .state("sign_up", {
        url: "/sign_up",
        templateUrl: "/static/accounts/views/sign_up/sign_up.html",
        controller: "SignUpController"
      })
      .state("log_in", {
        url: "/log_in",
        templateUrl: "/static/accounts/views/log_in/log_in.html",
        controller: "LogInController"
      });
  }

  angular.module("app")
    .config(["$stateProvider", AccountsRouterConfig]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function HomeRouterConfig($stateProvider) {
    $stateProvider.state("home", {
      url: "/",
      templateUrl: "/static/home/views/home/home.html",
      controller: "HomeController"
    });
  }

  angular.module("app")
    .config(["$stateProvider", HomeRouterConfig]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function AccountsModel($cookies) {
    var service = {
      clearUser: clearUser,
      getUser: getUser,
      hasUser: hasUser,
      setUser: setUser
    };

    function clearUser() {
      $cookies.remove("authenticatedUser");
    }

    function getUser() {
      if (!$cookies.get("authenticatedUser")) {
        return undefined;
      }

      return JSON.parse($cookies.get("authenticatedUser"));
    }

    function hasUser() {
      return !!$cookies.get("authenticatedUser");
    }

    function setUser(data) {
      $cookies.put("authenticatedUser", JSON.stringify(data.user));
    }

    return service;
  }

  angular.module("app")
    .factory("AccountsModel", ["$cookies", AccountsModel]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function accountsService($http, AccountsModel) {
    var service = {
      getUser: getUser,
      hasUser: hasUser,
      logIn: logIn,
      logOut: logOut,
      signUp: signUp
    };

    function getUser() {
      return AccountsModel.getUser();
    }

    function hasUser() {
      return AccountsModel.hasUser();
    }

    function logIn(username, password) {
      return $http.post("/accounts/log_in/", {
        username: username,
        password: password
      }).then(function (response) {
        AccountsModel.setUser(response.data);
      });
    }

    function logOut() {
      return $http.post("/accounts/log_out/", {}).then(function (response) {
        AccountsModel.clearUser();
      }, function () {
        console.error("Log out failed!");
      });
    }

    function signUp(firstName, lastName, email, password) {
      return $http.post("/accounts/sign_up/", {
        first_name: firstName,
        last_name: lastName,
        username: email,
        email: email,
        password: password
      }).then(function () {
        return logIn(email, password);
      });
    }

    return service;
  }

  angular.module("app")
    .factory("accountsService", ["$http", "AccountsModel", accountsService]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function LogInController($scope, $state, accountsService) {
    $scope.error = {};
    $scope.form = "";
    $scope.password = "";
    $scope.username = "";

    $scope.hasError = function hasError() {
      return !_.isEmpty($scope.error);
    };

    $scope.onSubmit = function onSubmit() {
      accountsService.logIn($scope.username, $scope.password).then(function () {
        $state.go("home");
      }, function (response) {
        $scope.error = response.data;
        $scope.password = "";
      });
    };
  }

  angular.module("app")
    .controller("LogInController", ["$scope", "$state", "accountsService", LogInController]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function HomeController($scope, accountsService) {
    $scope.hasUser = function hasUser() {
      return accountsService.hasUser();
    };
  }

  angular.module("app")
    .controller("HomeController", ["$scope", "accountsService", HomeController]);

})(window, window.angular);
(function (window, angular, undefined) {

  "use strict";

  function SignUpController($scope, $state, accountsService) {
    $scope.email = "";
    $scope.error = {};
    $scope.firstName = "";
    $scope.form = "";
    $scope.lastName = "";
    $scope.password1 = "";
    $scope.password2 = "";

    $scope.hasError = function hasError() {
      return !_.isEmpty($scope.error);
    };

    $scope.onSubmit = function onSubmit() {
      accountsService.signUp($scope.firstName, $scope.lastName, $scope.email, $scope.password1).then(function () {
        $state.go("home");
      }, function (response) {
        $scope.error = response.data;
        $scope.email = "";
        $scope.password1 = "";
        $scope.password2 = "";
      });
    };
  }

  angular.module("app")
    .controller("SignUpController", ["$scope", "$state", "accountsService", SignUpController]);

})(window, window.angular);