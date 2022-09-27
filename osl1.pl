# To write a Perl program to demonstrate Scalar values, Basic Operators 
# and control flow, List and array variables.
# scalar values 
$x=10;
$y=-10;
$z=10.1;
$string="krishraaj";


print($string." is my name.\n");
print($x."\n");
print($y."\n");
print($z."\n");

# Aritmetic operations,functions
$n1=100;
$n2=20;
$sum=$n1+$n2;
$sub=$n1-$n2;
$div=$n1/$n2;
$multi=$n1*$n2;

print("Multiplication: ".$multi."\n");
print("Division: ".$div."\n");
print("addition: ".$sum."\n");
print("Subtraction: ".$sub."\n");
print(exp($n1));
print(sqrt(10));
print(int(5));
print(rand(10));



# Comparing Scalars
# control flow 

# decision making 
$str = "krishraaj";
   
if($str == "krishraaj")
{
    print "\n== doesn't work with string values!\n";
   
}
   
# comparing with capital string
elsif($str eq "krishraaj")
{
    print "eq works with string values\n";
}

else{
     print "No match founded\n";
}

unless($a != 10)
{
    print( "a is not equal to 10\n");
}

for ($i = 1 ; $i <= 3 ; $i++)
{
    print ("Hello mam\n");
}
 
# do..While loop
do {
 
    print "$a ";
    $a = $a - 1;
} while ($a > 0);
# array list
@array = (10, 20, 30, 40, 50);

foreach $number (@array)
{
    print($number);
    print(" ");
}

print("\nList declared and printed: ");
print(10, 20, 30, 40, 50);


