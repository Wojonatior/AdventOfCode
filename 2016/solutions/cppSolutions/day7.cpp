//
// Created by Jarek Wojciechowski on 3/10/17.
//

#import "day7.h"
#import <fstream>
#import <iostream>

//Checks for an abba pattern in the string starting at i
// abba allowed
// aaaa not allowed
bool check_abba(std::string address, int i){
    return (address[i] == address[i+3]) && (address[i+1] == address[i+2]) && (address[i] != address[i+1]);
}

int find_closing_bracket(std::string address, int start){
    for (int i=start; i<address.length(); i++)
        if(address[i] == ']')
            return i;
}

bool abba_in_brackets(std::string address, int start, int end){
    for(int i=start; i < end; i++){
        if (check_abba(address, i)){ return true; }
    }
}

bool validate_ipv7(std::string address){
    // [abcd]   used to visualize the indexes
    // i12345
    // If there is an abba pattern within the brackets, the address is invalid
    for(int i=0; i < address.length(); i++){
       if(address[i] == '['){
           if(abba_in_brackets(address, i, find_closing_bracket(address, i))){
               return false;
           }
       }
    }
    // If there is an abba pattern anywhere else within the string the address is valid
    for(int i=0; i < address.length()-3; i++)
        if (check_abba(address, i))
            return true;
    // Otherwise the address is invalid
    return false;
}

void test_validation_method(std::string address, int case_num, bool expected_result){
    // xnor used to return true when the expected result and the function call match
    if(!(validate_ipv7(address) ^ expected_result))
        std::cout << "Case " << case_num << " Passed\n";
    else
        std::cout << "Case " << case_num << " Failed\n";
}

int solve_day7(bool testing){
    FILE *fp;
    if ((fp = fopen("day7input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    int valid_addresses = 0;
    char temp_cstr[256];
    std::string ipv7_address;

    while (fscanf(fp, "%s", &temp_cstr) > 0) {
        ipv7_address = temp_cstr;
        if( validate_ipv7(ipv7_address))
            valid_addresses++;

    }

    if(testing){
        test_validation_method("abba[mnop]qrst", 1, true);
        test_validation_method("abcd[bddb]xyyx", 2, false);
        test_validation_method("aaaa[qwer]tyui", 3, false);
        test_validation_method("ioxxoj[asdfgh]zxcvbn", 4, true);
    }

    std::cout << "Number of Valid IPV7 Addresses: " << valid_addresses;
}
