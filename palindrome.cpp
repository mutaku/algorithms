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

using namespace std;

int factorize(int product){
    return 0;
}

int get_digits(){
    // retrieve digits for factor size from user
    int number_digits;
    cout << " >> Enter number of digits: " << endl;
    cin >> number_digits;
    return number_digits;
}
string int_to_string(unsigned long int number){
    // convert integer to string
    stringstream ss;
    ss << number;
    return ss.str();
}
string halve_integer(unsigned long int number, int half_size){
    // split a number in half
    string full_number = int_to_string(number);
    cout << full_number << endl;
    string half = full_number.substr(0, half_size);
    cout << half << endl;
    return half;
}
int main(){
    // get number of digits for factor size
    int factor_size = get_digits();
    // product magnitude
    int magnitude = factor_size * 2;
    // maximum, or start iteration value
    unsigned long int start = pow((double)10, magnitude) - 1;
    unsigned long int counter = start;
    // Cut the number into symmetrical elements
    // we will then flip to make palindromes
    string symmetry = halve_integer(start, factor_size);
}