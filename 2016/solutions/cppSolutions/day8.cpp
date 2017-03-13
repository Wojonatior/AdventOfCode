//
// Created by Jarek Wojciechowski on 3/12/17.
//
#include <iostream>
#include <fstream>
#include <regex>

class Screen{
    int pixels[6][50] = {{0}};
public:
    Screen(){}
    int how_many_lit(){
        int lit_count = 0;
        for(int i=0; i<6; i++)
            for(int j=0; j<50; j++)
               if (pixels[i][j] == 1)
                  lit_count++;
        return lit_count;
    };

    void rectangle(int x, int y){
        for(int i=0; i<x; i++)
            for(int j=0; j<y; j++){
                pixels[i][j] == 1;
                std::cout << "pixel lit\n";
            }
    }
    void rotate_column(int column_number, int distance){return;}
    void rotate_row(int column_number, int distance){return;}
};

int solve_day8(){
    FILE *fp;
    if ((fp = fopen("day8input.txt", "r+")) == NULL) {
        printf("File doesn't exist\n");
        exit(1);
    }

    char instruction[256];
    //std::string instruction;
    Screen screen = Screen();
    char instr_type;

    //rect 3x2
    //rotate column x=1 by 1
//    while (fscanf(fp, "rotate %*s %c=%d by %d", &instr_type, &line_num, &trans_dist) ||
//            fscanf(fp, "%c%*s %dx%d", &instr_type, &x, &y) > 0){
    while(fgets(instruction, 256, fp)){
    //while (fscanf(fp, "%[^\n]", &instruction) != 0) {
        std::cout << instruction << "\n";
        std::cmatch response;
        std::regex rectangle_rx("rect (\\d)*x(\\d)*");
        std::regex translate_rx("rotate ((row)?(column)?) [xy]=(\\d*) by (\\d*)");

        std::regex_search(instruction, response, rectangle_rx);
        if(response.length()>1){
            std::cout << response[1] << " " << response[2];
//            screen.rectangle(stoi(response[1]), stoi(response[2]));
            std::cout << "rectangle\n";
        }
        else {
            std::regex_search(instruction, response, rectangle_rx);
            if(response[1] == "row"){
                //screen.rotate_row(std::stoi(response[4]), std::stoi(response[5]));
                std::cout << "row\n";
            }else{
//                screen.rotate_column(std::stoi(response[4]), std::stoi(response[5]));
                std::cout << "column\n";
            }
        }
    }

    std::cout << "Number of pixels lit: " << screen.how_many_lit();
}
