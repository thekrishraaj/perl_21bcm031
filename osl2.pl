#check if email is valid
use strict;
use warnings;

#USE OF SUBROUTINES
sub is_valid_email {
    my $email = shift;
    #USE OF REGEX TO CHECK IF EMAIL IS VALID
    if ($email =~ /^[\w\d]+\@[\w\d]+\.[\w\d]+$/) {
        return 1;
    }
    else {
        return 0;
    }
}

print "Enter email: ";
my $email = <STDIN>;
chomp $email;
if (is_valid_email($email)) {
    print "Valid email\n";
}
else {
    print "Invalid email\n";
}

#use of hash
my $l = {1 => "Rudra", 2 => "good boy"};
print($l->{1});