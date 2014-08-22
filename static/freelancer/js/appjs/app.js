/**
 * Created by kevin on 8/16/2014.
 */
 
// Should split this out into multiple files
var editApp = angular.module("editApp", ["xeditable", "ngResource"]);
editApp.run(function (editableOptions) {
    editableOptions.theme = 'bs3';
});

editApp.factory('editFactory', function ($resource) {
    return $resource('http://myportfoliorockss.herokuapp.com/api/v1/user/' + userId + '/', {})
});

editApp.controller('editController', function ($scope, editFactory, $http) {
    // This looks like it could be made better and not defaulted like this
    $scope.user = {};
    $scope.user['header'] = "MyPortfolio.rocks";
    $scope.user['fblink'] = "http://www.facebook.com";
    $scope.user['googlelink'] = "http://www.google.com";
    $scope.user['twitterlink'] = "http://www.twitter.com";
    $scope.user['linkedin'] = "http://www.linkedin.com";
    $scope.user['dribble'] = "httpL//www.dribble.com";
    $scope.user['about1'] = "Tell the world about who you are here";
    $scope.user['about2'] = "Tell us more";
    $scope.user['name'] = "Your Name";
    $scope.user['skills'] = "angular - django - python - tastypie - jquery";
    $scope.user['location'] = "Location";
    $scope.user['address'] = "157 Sutter St, San Francisco, CA";
    $scope.user['aroundtheweb'] = 'Around The Web';
    editFactory.get(function (response) {
        for (var i = 0; i < response.text.length; i++) {
            $scope.user[response.text[i].html_id] = response.text[i].text
        }
        console.log($scope.user);
    });
//    $scope.project={title:'title', body:'body'};

    $scope.updateUser = function () {
        console.log($scope.user);
//        console.log($scope.project);
        $http.post('/update/', $scope.user);
        return $scope.user;
    };

    // Don't use jQuery in your Angular controllers!!!!
    if (disabled) {
        console.log("hello");
        var $editable=$('.editable');
        $editable.removeClass('editable-click');
        $editable.unbind('click');
        $('.btn-social').removeClass('editable');
    }
//    $scope.show = function(form){
//        if ($scope.allDisabled == true){
//            console.log("yeay");
//            form.$show();
//        }
//    };
//    $scope.show = function(form){
//        if ($scope.allDisabled= true){
//            form.$show();
//        }
//    }
});

editApp.controller('projectController', function ($scope, editFactory, $http, $compile) {
    $scope.project = {};
    editFactory.get(function (response) {
        for (var i = 0; i < response.project.length; i++) {
            var project = response.project[i];
            $scope.project[project.id] = {image: project.image, title: project.title, description: project.description}
        }
    });
    $scope.addProject = function () {
        $http.get('/newproject/').success(function (response) {
            var thumbnail = angular.element(response);
            var projectId = thumbnail.data('id');
            $http.get('/newproject_modal/' + projectId).success(function (modal) {
//                var modal = $compile(response);
                angular.element(document.querySelector('#modalcontainer')).append($compile(modal)($scope));
                var target = angular.element(document.querySelector('#portfolioThumbnail'));
                target.append(thumbnail);
            })
        })
    };
    $scope.deleteProject = function (event) {
        var project_id = angular.element(event.srcElement);
        $http.get('/delete_project/' + project_id);

    };

    $scope.updateProject = function () {
        console.log($scope.project);
        $http.post('/update_project/', $scope.project);
        return $scope.project;
    }
});

editApp.directive("addbuttonsbutton", function () {
    return {
        restrict: "E",
        template: "<button addbuttons>Click to add buttons</button>"
    }
});


//editApp.directive("addbuttons", function($compile){
//    return function(scope, element, attrs){
//        console.log("yea");
//
//        element.bind("click", function(){
//            angular.element(document.getElementById('space-for-buttons')).append($compile(portfolioTemplate)(scope));
//
//        })
//    }
//})


//editApp.controller('ProjectController', function($scope){
//    $scope.addProject = function(){
//        var newProject =
//    }
//})
//
//$(document).ready(function(){
//    if (disabled) {
//        var $editable=$('.editable');
//        $editable.removeClass('editable-click');
//        $editable.unbind('click');
//    }
//})
