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
      $cookies.remove("pdsAuthenticatedUser");
    }

    function getUser() {
      if (!$cookies.get("pdsAuthenticatedUser")) {
        return undefined;
      }

      return JSON.parse($cookies.get("pdsAuthenticatedUser"));
    }

    function hasUser() {
      return !!$cookies.get("pdsAuthenticatedUser");
    }

    function setUser(data) {
      $cookies.put("pdsAuthenticatedUser", JSON.stringify(data.user));
    }

    return service;
  }

  angular.module("app")
    .factory("AccountsModel", ["$cookies", AccountsModel]);

})(window, window.angular);