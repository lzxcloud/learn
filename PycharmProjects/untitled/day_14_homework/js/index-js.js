/**
 * Created by lanzexi on 16/10/19.
 */
var input_user_error =[false,"none","用户名"];
var input_passwd_error=[false,"none","密码"];
var input_id_error=[false,"none","昵称"];
function CheckRegex(ths,name,action,id) {
    var this_value = ths.value;
    var user_regex = /^([0-9A-Za-z\-_\.]+)@([0-9a-z]+\.[a-z]{2,3}(\.[a-z]{2})?)$/g;
    var passwd_regex = /(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{8,30}/g;
    var id_regex = /[a-zA-Z0-9]\w{5,12}]/g;
    function chang_style(color,error_id,error_code,error_txt) {
        if (color == "red"){
            ths.style.border="1px solid red";
            error_id[0]=false;
            error_id[1]=error_code;
            error_id[2]=error_txt;
            return false
        }else if (color == "green"){
            ths.style.border="1px solid green";
            error_id[0]=true;
            error_id[1]="";
            error_id[2]="";
            return false;
        }
    }
    if (name == "username") {
        if (action == "leave") {
            if (this_value == "") {
                chang_style("red",input_user_error,"none","用户名");
            } else if (user_regex.test(this_value)){
                chang_style("green",input_user_error);
            } else {
                chang_style("red",input_user_error,"error","用户名");
            }
        } else if (action == "on") {
            // ths.style.border = "1px solid #dfebf2";
        }
    }else if(name=="passwd"){
        if (action=="leave"){
            if (this_value == ""){
                chang_style("red",input_passwd_error,"none","密码");
            } else if(passwd_regex.test(this_value)){
                chang_style("green",input_passwd_error);
            }else{
                chang_style("red",input_passwd_error,"error","密码");
            }
        }else if(action == "on"){
            // ths.style.border = "1px solid #dfebf2";
        }
    }else if(name == "id"){
        if(action == "leave"){
            if (this_value == "") {
                chang_style("red",input_id_error);

            }else if (id_regex.test(this_value)){
                chang_style("green",input_id_error);
            }
        }else if (action == "on"){
        }
    }
}
function login(){
    if (input_user_error[0]==true && input_passwd_error[0]==true) {
        show_error_msg("3");
    }else if (input_user_error[1]=="none"||input_passwd_error[1]=="none"){
        setTimeout(show_error_msg("1"),5000);
    } else if (input_user_error[1]=="error"||input_passwd_error[1]== "error"){
        show_error_msg("2");
    }
}
function ConfirmPasswd(ths) {
    passwd = document.getElementsByTagName("input")[2]
}
function Register() {
     if (input_user_error[0]==true && input_passwd_error[0]==true && input_id_error[0]) {
        window.open()
     }else if (input_user_error[1]=="none"||input_passwd_error[1]=="none"||input_id_error[1]){
        window.alert("请输入"+input_id_error);
    } else if (input_user_error[1]=="error"||input_passwd_error[1]== "error"||input_id_error[1]){
        window.alert(input_user_error[2]+input_passwd_error[2]+input_id_error[2]+"输入有误")
    }
}
function show_error_msg(flag) {
    thss = document.getElementById("error-msg");
    while (input_user_error[0]==true && input_passwd_error[0]==true){
        if (input_user_error[0]==true && input_passwd_error[0]==true){
            thss.classList.add("hide")
        }
    }
    if(flag=="1"){
        thss.classList.remove("hide");
        thss.innerText = "请输入"+input_user_error[2] + input_passwd_error[2]
        overflow = hide
    }else if(flag=="2"){
        thss.classList.remove("hide");
        thss.innerText = input_user_error[2] + input_passwd_error[2] +"输入有误"
    }

    while (input_user_error[0]==true && input_passwd_error[0]==true){
        if (input_user_error[0]==true && input_passwd_error[0]==true){
            thss.classList.add("hide")
        }
    }
}