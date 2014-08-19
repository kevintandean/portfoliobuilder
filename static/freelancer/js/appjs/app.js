/**
 * Created by kevin on 8/16/2014.
 */
var editApp = angular.module("editApp", ["xeditable", "ngResource"]);
editApp.run(function(editableOptions){
    editableOptions.theme = 'bs3';
});

editApp.factory('editFactory', function($resource){
    return $resource('http://127.0.0.1:8000/api/v1/user/'+userId+'/', {})
});

editApp.controller('editController', function($scope, editFactory, $http){
    $scope.user={};
    $scope.user['fblink']="http://www.facebook.com";
    $scope.user['googlelink']="google.com";
    $scope.user['twitterlink']="twitter.com";
    editFactory.get(function(response){
        for (var i=0; i < response.text.length; i++){
            $scope.user[response.text[i].html_id]=response.text[i].text
        }
        console.log($scope.user);
    });
//    $scope.project={title:'title', body:'body'};

    $scope.updateUser = function() {
        console.log($scope.user);
//        console.log($scope.project);
        $http.post('/update/', $scope.user);
        return $scope.user;

    }
});

editApp.controller('projectController', function($scope, editFactory, $http, $compile){
    $scope.project={};
    editFactory.get(function(response){
        for (var i=0; i<response.project.length; i++){
            var project = response.project[i];
            $scope.project[project.id] = {image: project.image, title: project.title, description: project.description}
        }
    });
    $scope.addProject = function(){
        $http.get('/newproject/').success(function(response){
            var thumbnail = angular.element(response);
            var projectId = thumbnail.data('id');
            $http.get('/newproject_modal/'+projectId).success(function(modal){
//                var modal = $compile(response);
                angular.element(document.querySelector('#modalcontainer')).append($compile(modal)($scope));
                var target = angular.element(document.querySelector('#portfolioThumbnail'));
                target.append(thumbnail);
            })

        })
    };
    $scope.deleteProject = function(event){
        var project_id = angular.element(event.srcElement);
        $http.get('/delete_project/'+project_id);

    };

    $scope.updateProject = function() {
        console.log($scope.project);
    }
});

editApp.directive("addbuttonsbutton", function(){
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