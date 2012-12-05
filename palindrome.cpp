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

pair<long long, long long> factorize(long long product){
    // square sieving to search for factors
    long long symmetry;
    symmetry = floor(sqrt(product) + 0.5);
    int mag;
    mag = floor(log10(product)) + 1;
    long long factor_ceiling, factor_floor;
    factor_ceiling = pow((double)10, (mag / 2)) - 1;
    factor_floor = symmetry - (factor_ceiling - symmetry);
    long long high, low;
    if (pow((double)factor_ceiling, 2) < product){
        high = 0;
        low = 0;
    } else {
        while(1){
            // find factors
        }
    }
    return make_pair(high, low);
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
    // stop point for n by n digit factor products
    // we should not hit this else we have no 
    // palindromes
    long long stop = pow((double)10, (factor_size - 1));

    // Cut the number into symmetrical elements
    // we will then flip to make palindromes
    // convert number into string and take first half substring
    string number_string = as_string(start);
    string symmetry_string = number_string.substr(0, factor_size);
    long long symmetry = as_int(symmetry_string);
    // ------------------------------------------------------------
    // debugging things and making sure our conversions are working
    cout << symmetry << " - symmetry" << endl;
    cout << "start " << start << " - stop " << stop << endl;
    long long test_int = 5;
    string test_str = "5";
    cout << typeid(symmetry).name() << typeid(test_int).name() << end
l;
    cout << typeid(symmetry_string).name() << typeid(test_str).name()
 << endl;
    // end debugging stuffs 
    // ------------------------------------------------------------
    long long factor_i;
    long long factor_j;
    long long max_pali;
    long long num;
    while (symmetry >= stop){
        symmetry_string = as_string(symmetry);
        num = as_int(symmetry_string + 
                string (symmetry_string.rbegin(), 
                    symmetry_string.rend()));
        cout << num << endl;
        // check this palindrome now
        // finally, increment our counters down
        symmetry = as_int(symmetry_string);
        symmetry--;
        cout << symmetry << endl;
    }
}