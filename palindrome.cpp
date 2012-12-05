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

struct Factors {
    long long i;
    long long j;
};

Factors factorize(long long product){
    // square sieving to search for factors
    long long symmetry;
    symmetry = floor(sqrt(product) + 0.5);
    int mag;
    mag = floor(log10(product)) + 1;
    long long factor_ceiling, factor_floor;
    factor_ceiling = pow((double)10, (mag / 2)) - 1;
    factor_floor = symmetry - (factor_ceiling - symmetry);
    Factors results = { 0, 0 };
    long long low_high_product;
    if (pow((double)factor_ceiling, 2) < product){
        while(1){
            low_high_product = results.i * results.j;
            if (low_high_product == product){
                break;
            } else if (results.j < factor_floor ||
                    results.i < factor_floor){
                results.i  = 0;
                results.j = 0;
                break;
            } else if (results.j > factor_ceiling ||
                    results.i > factor_ceiling){
                results.i  = 0;
                results.j = 0;
                break;
            } else if (low_high_product < product){
                results.j++;
            } else if (low_high_product > product){
                results.i--;
            }
        }
    }
    return results;
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
    cout << typeid(symmetry).name() << typeid(test_int).name() << endl;
    cout << typeid(symmetry_string).name() << typeid(test_str).name() << endl;
    // end debugging stuffs 
    // ------------------------------------------------------------
    long long max_pali;
    long long num;
    Factors results;
    while (symmetry >= stop){
        symmetry_string = as_string(symmetry);
        num = as_int(symmetry_string + 
                string (symmetry_string.rbegin(), 
                    symmetry_string.rend()));
        // check this palindrome now
        results = factorize(num);
        if (results.i != 0 &&
                results.j != 0){
            break;
        }
        // finally, increment our counters down
        symmetry = as_int(symmetry_string);
        symmetry--;
    }
    cout << results.i << " , " << results.j << " , " << num << endl;
    return 0;
}