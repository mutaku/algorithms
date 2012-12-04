/* palindrome.cpp
 * C++ implementation of palindrome.py
 * (https://gist.github.com/4081368)
 *
 * - Matthew Martz 2012
 */

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

// includes for testing only
#include <typeinfo>

using namespace std;

int factorize(int product){
    return 0;
}

int get_digits(){
    // retrieve digits for factor size from user
    int number_digits;
    cout << " Enter number of digits: " << endl;
    cin >> number_digits;
    return number_digits;
}

string as_string(long long number){
    // convert integer to string
    stringstream ss;
    ss << number;
    return ss.str();
}

long long as_int(string number){
    // convert string number to int number
    return atoi(number.c_str());
}

int main(){
    // get number of digits for factor size
    int factor_size = get_digits();
    // product magnitude
    int magnitude = factor_size * 2;
    // maximum, or start iteration value
    long long start = pow((double)10, magnitude) - 1;
    long long counter = start;
    // Cut the number into symmetrical elements
    // we will then flip to make palindromes
    // convert number into string and take first half substring
    string number_string = as_string(start);
    string symmetry_string = number_string.substr(0, factor_size);
    long long symmetry = as_int(symmetry_string);

    // debugging things and making sure our conversions are working
    cout << symmetry << " - symmetry" << endl;
    long long test_int = 5;
    string test_str = "5";
    cout << typeid(symmetry).name() << typeid(test_int).name() << endl;
    cout << typeid(symmetry_string).name() << typeid(test_str).name() << endl;
}