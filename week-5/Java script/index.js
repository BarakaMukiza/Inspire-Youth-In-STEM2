
            // variables in javascript
            //number
            var num = 12;
            var f_number = 20;
            var s_number = 10;
            var sum_num= f_number+s_number;

            //string
            var my_first_name = "Baraka";
            var my_second_name = "Mukiza";
            var age =  20;
            var weight = 86.9;

            var full_name = my_first_name+" "+ my_second_name
            //arithmetic operators
            var n1=5;
            var n2=6;
            var sum = n1+n2;
            var diff = n2-n1;
            var  pro = n1*n2;
            var quotient =  n2/n1;
            var modulus = n2%n1;
            var float = 34.6;

            var n1,n2,n3,n4 ; //declare variables

            
            document.getElementById("f_number").innerHTML = f_number;//used to link javascript with html and get the element
            document.getElementById("s_number").innerHTML = s_number;
            document.getElementById("sum_num").innerHTML = sum_num;
            
            /*
            document.getElementById("f_name").innerHTML = my_first_name;
            document.getElementById("s_name").innerHTML = my_second_name;
            document.getElementById("age").innerHTML = age;
            document.getElementById("weight").innerHTML = weight;
            */
            document.getElementById("full_name").innerHTML = full_name;

            //arrays
            let fruits=["banana","apples","avocado","lemon","peaches"];
            let myfruit = fruits[fruits.length -1];//gives you the last element
            document.getElementById("myfruit").innerHTML = myfruit;
            
            //conditions
            if (age>=18){
                var msg = "you can drive"
            }else{
                var msg = " you are too young to drive."
            }
            document.getElementById("myfruit").innerHTML = msg;


            