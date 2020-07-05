<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    {%block title %}
    <title>Covid19 Tracker</title>

    <meta name="description" content="Covid19 Data of Morocco and the World." />
    <meta name="keywords"
        content="covid19" />
    <meta name="author" content="covid19" />
    {% endblock title %}

    <!-- Favicon -->
    <link rel="icon" href="dist/img/favicon.ico">

    <link href="static/vendors/bower_components/datatables/media/css/jquery.dataTables.min.css" rel="stylesheet"
        type="text/css" />

    <!-- toast -->
    <link href="static/vendors/bower_components/jquery-toast-plugin/dist/jquery.toast.min.css" rel="stylesheet"
        type="text/css">

        <!-- bootstrap select -->
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/css/bootstrap-select.min.css"> -->


    <!-- Custom CSS -->
    <link href="static/dist/css/style.css" rel="stylesheet" type="text/css">
 <!-- select2 -->
 <link href="https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css" rel="stylesheet" />

</head>

<body>
    <!-- Preloader -->
    <div class="preloader-it">
        <div class="la-anim-1"></div>
    </div>
    <!-- /Preloader -->
    <div class="wrapper  theme-6-active pimary-color-blue">
        <!-- Top Menu Items -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="mobile-only-brand pull-left">
                <div class="nav-header pull-left">
                    <div class="logo-wrap">
                        <a href="index.html">
                            <img class="brand-img" src="static/dist/img/logo.png" alt="brand"
                                style="width: 22px;" />
                            <span class="brand-text">Covid19</span>
                        </a>
                    </div>
                </div>
                <a id="toggle_nav_btn" class="toggle-left-nav-btn inline-block ml-20 pull-left"
                    href="javascript:void(0);"><i class="zmdi zmdi-menu"></i></a>
                <a id="toggle_mobile_search" data-toggle="collapse" data-target="#search_form" class="mobile-only-view"
                    href="javascript:search();"><i class="zmdi zmdi-search"></i></a>
                <a id="toggle_mobile_nav" class="mobile-only-view" href="javascript:search();"><i
                        class="zmdi zmdi-more"></i></a>
                <form autocomplete="off" id="search_form" role="search" class="top-nav-search collapse pull-left">
                    <div class="input-group">
                        <input type="text" name="country" class="form-control"
                            placeholder="Enter country name" style="text-transform: none!important;">
                        <span class="input-group-btn">
                            <button type="button" class="btn  btn-default" data-target="#search_form"
                                data-toggle="collapse" aria-label="Close" aria-expanded="true" onclick="document.getElementById('search_form').submit(); return false;"><i
                                    class="zmdi zmdi-search"></i></button>
                        </span>
                    </div>
                </form>

            </div>

        </nav>
        <!-- /Top Menu Items -->

        <!-- Left Sidebar Menu -->
        <div class="fixed-sidebar-left">
            <ul class="nav navbar-nav side-nav nicescroll-bar">
                <li class="navigation-header">
                    <span>Menu</span>
                    <i class="zmdi zmdi-more"></i>
                </li>
                <li>
                    <a href="info/templates/info/information.html" data-toggle="collapse" data-target="#Information">
                        <div class="pull-left"><img style="margin-right: 8px;" src="static/dist/img/who.png"
                                width="20"><span class="right-nav-text">Covid-19 Information</span></div>
                        <div class="clearfix"></div>
                    </a>
                </li>
                <li>
                    <a  href="javascript:void(0);" data-toggle="collapse" data-target="#country">
                        <div class="pull-left "><img class="mr-10 mt-5"
                                src="https://www.countryflags.io/MA/flat/16.png "><span class="right-nav-text">Moroccan
                                Overall Report</span>
                        </div>
                        <!-- <div class="pull-right"><span class="label label-primary">Güncel</span></div> -->
                        <div class="clearfix"></div>
                    </a>
                    <ul id="country" class="collapse collapse-level-1">
                        <li>
                            <a href="info/templates/info/country.html">General Data</a>
                        </li>
                        <li>
                            <a href="info/templates/info/moroccan_plots.html">Plots
                                of Morocco</a>
                        </li>
                    </ul>
                </li>

                <li>
                    <a  href="javascript:void(0);" data-toggle="collapse" data-target="#world">
                        <div class="pull-left"><i class="zmdi zmdi-google-earth mr-10"></i><span
                                class="right-nav-text">Worldwide Report</span></div>

                        <div class="pull-right"><span class="label label-primary"></span></div>
                        <div class="clearfix"></div>
                    </a>
                    <ul id="world" class="collapse collapse-level-1">
                        <li>
                            <a href="{% url 'world' %}">General worldwide Data</a>
                        </li>
                        <li>
                            <a href="{% url 'world_plots' %}">World Plots</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a  href="javascript:void(0);" data-toggle="collapse" data-target="#symptom">
                        <div class="pull-left"><i class="zmdi zmdi-hospital mr-10"></i><span
                                class="right-nav-text">Is covid near you ?</span></div>

                        <div class="pull-right"><span class="label label-primary"></span></div>
                        <div class="clearfix"></div>
                    </a>
                    <ul id="symptom" class="collapse collapse-level-1">
                        <li>
                            <a href="{% url 'uti_new' %}">Report cases</a>
                        </li>
                        <li>
                            <a href="{% url 'uti_list' %}">List of cases</a>
                        </li>
                    </ul>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="#">
                  </a>
                </li>
                <li class="nav-item">
                  <a name="deco" class="nav-link" href="{% url 'registration' %}">
                    <div class="pull-left"><i class="zmdi zmdi-power-setting mr-10"></i><span
                          class="right-nav-text">Logout</span></div>

                    <div class="pull-right"><span class="label label-primary"></span></div>
                    <div class="clearfix"></div>
                  </a>
                </li>
                <li>
                    <a  href="javascript:void(0);" data-toggle="collapse" data-target="#contact">
                        <div class="pull-left "><i class="zmdi zmdi-comment-text mr-10"></i><span class="right-nav-text">Contact Us</span>
                        </div>
                        <div class="clearfix"></div>
                    </a>
                    <ul id="contact" class="collapse collapse-level-1">
                        <li>
                            <a href="https://www.facebook.com/Mohamed.elkhatiri10">
                              <div class="pull-left "><i class="zmdi zmdi-facebook mr-10"></i><span class="right-nav-text">Facebook</span>
                              </div>
                              <div class="clearfix"></div>
                            </a>
                        </li>
                        <li>
                          <a href="https://twitter.com/mohamed70336793?s=09">
                            <div class="pull-left "><i class="zmdi zmdi-twitter mr-10"></i><span class="right-nav-text">Twitter</span>
                            </div>
                            <div class="clearfix"></div>
                          </a>
                        </li>
                        <li>
                          <a href="https://www.instagram.com/medelkhatiri/">
                            <div class="pull-left "><i class="zmdi zmdi-instagram mr-10"></i><span class="right-nav-text">Instargram</span>
                            </div>
                            <div class="clearfix"></div>
                          </a>
                        </li>
                        <li>
                          <a href="https://github.com/medel96">
                            <div class="pull-left "><i class="zmdi zmdi-github mr-10"></i><span class="right-nav-text">Github</span>
                            </div>
                            <div class="clearfix"></div>
                          </a>
                        </li>
                        <li>
                          <a href="#">
                            <div class="pull-left "><i class="zmdi zmdi-google mr-10"></i><span class="right-nav-text">Email : </br>medelkhatiri@gmail.com</span>
                            </div>
                            <div class="clearfix"></div>
                          </a>
                        </li>
                    </ul>
                </li>


            </ul>
        </div>
        <div class="page-wrapper">
            <div class="container-fluid pt-25">
                <div class="row">




                    <!----------------------------- ----------Main Content------------------------- -->
                    {% block content %}


                    {% endblock content %}

                </div>
            </div>
        </div>


        <!-- JavaScript -->


        <!-- jQuery -->
        <script src="{% static 'vendors/bower_components/jquery/dist/jquery.min.js' %}"></script>

        <!-- Typed.js -->
        <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.11"></script>


        <!-- Chart.js CDN-->
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

        <!-- Moment.js -->

        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment-with-locales.min.js"></script>




        <!-- Bootstrap Core JavaScript -->
        <script src="{% static 'vendors/bower_components/bootstrap/dist/js/bootstrap.min.js' %}"></script>


        <!-- Bootstrap Select -->

        <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.14/dist/js/bootstrap-select.min.js"></script> -->



        <!-- Data table JavaScript -->
        <script src="{% static 'vendors/bower_components/datatables/media/js/jquery.dataTables.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/datatables.net-buttons/js/dataTables.buttons.min.js' %}">
        </script>
        <script src="{% static 'vendors/bower_components/datatables.net-buttons/js/buttons.flash.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/jszip/dist/jszip.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/pdfmake/build/pdfmake.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/pdfmake/build/vfs_fonts.js' %}"></script>

        <script src="{% static 'vendors/bower_components/datatables.net-buttons/js/buttons.html5.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/datatables.net-buttons/js/buttons.print.min.js' %}"></script>


        <!-- Slimscroll JavaScript -->
        <script src="{% static 'dist/js/jquery.slimscroll.js' %}"></script>



        <!-- Progressbar Animation JavaScript -->
        <script src="{% static 'vendors/bower_components/waypoints/lib/jquery.waypoints.min.js' %}"></script>
        <script src="{% static 'vendors/bower_components/jquery.counterup/jquery.counterup.min.js' %}"></script>



        <!-- Init JavaScript -->
        <script src="{% static 'dist/js/init.js' %}"></script>
        <script src="{% static 'dist/js/main.js' %}"></script>
          <!-- select2 -->
          <link href="https://cdn.jsdelivr.net/npm/select2@4.0.13/dist/css/select2.min.css" rel="stylesheet" />

        {% block js %}
        <script>
            var searchbar = document.querySelector(".search");

            function slide(){
              if (searchbar.classlist.contains("hide")){
                serchbar.classlist.remove("hide");
              }
              else{
                searchbar.classlist.add("hide");
              }
            }

        </script>
        {% endblock js %}
</body>

</html>
