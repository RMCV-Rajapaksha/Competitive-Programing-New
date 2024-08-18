#include <iostream>
#include <string>

using namespace std;

class Dancing {

public:
    string topR;
    string topL;

    string middleR;
    string middleL;

    string bottomR;
    string bottomL;

    //Head Commands 
    string one = "left hand to head";
    string two = "right hand to head";

    //Middle Commands
    string three = "left hand to hip";
    string four = "right hand to hip";
    string five = "left hand to start";
    string six = "right hand to start";

    //Leg Commands
    string seven = "left leg in";
    string eight = "left leg out";
    string nine = "right leg in";
    string ten = "right leg out";

    //Flip Body
    string eleven = "turn";

    //Functions
        //Head of Person
    void setTopL(string);
    void setTopR(string);

    //Arms
    void setMiddleL(string);
    void setMiddleR(string);

    //Legs of Person
    void setBottomR(string);
    void setBottomL(string);


    //Turn Function
    void setTurn();

};



int main()
{
    int T = 0; //Number of test cases]
    int d = 0;

    int repeat = 0;

    Dancing action;

    cin >> T; //low bound

    cin.ignore();

    string input;
    string tempStr;
    string interpret;
    for (int i = 0; i < T; i++) {
        cin >> d; //max commands
        repeat = 0;
        d += 1;
        for (int j = 0; j < d; j++) {

            getline(cin, input);
            tempStr = input;

            //Reads the first word of the input
            interpret = input.substr(0, input.find(" "));


            if (interpret == "say")
            {
                //Deletes first word of string (which should be say)
                tempStr = tempStr.substr(tempStr.find_first_of(" \t") + 1);

                cout << tempStr << endl;
            }
            else
            {
                //Default Person

                if (repeat == 0) {
                    action.topR = " o";
                    action.topL = " ";

                    action.middleR = "/|";
                    action.middleL = "\\";

                    action.bottomR = "/";
                    action.bottomL = "\\";
                    repeat++;
                }

                //Sets Head of Dancer
                if (tempStr == action.one)
                    action.setTopL(tempStr);

                if (tempStr == action.two)
                    action.setTopR(tempStr);


                //Sets Arms of Dancer

                else if (tempStr == action.three || tempStr == action.five)
                    action.setMiddleL(tempStr);


                else if (tempStr == action.four || tempStr == action.six)
                    action.setMiddleR(tempStr);


                //Sets Legs of Dancer
                else if (tempStr == action.seven || tempStr == action.eight)
                    action.setBottomL(tempStr);


                else if (tempStr == action.nine || tempStr == action.ten)
                    action.setBottomR(tempStr);

                //Turn Dancer Around 

                else if (tempStr == action.eleven)
                    action.setTurn();




                //Output 
                if (repeat > 1) {
                    cout << action.topR << action.topL << endl;
                    cout << action.middleR << action.middleL << endl;
                    cout << action.bottomR << " " << action.bottomL << endl;
                }
                repeat++;
            }
        }
    }
    return 0;
}


void Dancing::setTopR(string a)
{
    if (a == two)
    {
        topR = "(o";
        setMiddleR("clear");

    }

    else if (a == "clear")
    {
        topR = " o";
    }
}

void Dancing::setTopL(string a)
{
    if (a == one)
    {
        topL = ")";
        setMiddleL("clear");

    }
    else if (a == "clear")
    {
        topL = " ";
    }
}

void Dancing::setMiddleR(string a)
{
    if (a == four)
    {
        middleR = "<|";
        setTopR("clear");
    }


    else if (a == six)
    {
        middleR = "/|";
        setTopR("clear");
    }

    else if (a == "clear")
        middleR = " |";
}

void Dancing::setMiddleL(string a)
{
    if (a == three) {
        middleL = ">";
        setTopL("clear");
    }

    else if (a == five)
    {
        middleL = "\\";
        setTopL("clear");
    }


    else if (a == "clear")
        middleL = " ";
}

void Dancing::setBottomR(string a)
{
    if (a == nine)
        bottomR = "<";

    else if (a == ten)
        bottomR = "/";
}

void Dancing::setBottomL(string a)
{
    if (a == seven)
        bottomL = ">";

    else if (a == eight)
        bottomL = "\\";
}

void Dancing::setTurn()
{
    string tempL;
    string tempR;

    bool change = false;


    //Swap of Head
    tempL = topL;
    tempR = topR;

    tempR.erase(1);

    string sum;
    if (tempL == ")")
    {
        tempL = "(";
        change = true;
    }
    if (tempR == "(")
    {
        tempR = ")";
        change = true;
    }
    if (change == true)
    {
        tempL.append("o");
        topR = tempL;
        topL = tempR;
    }

    change = false;

    //Swap of Middle

    tempL = middleL;
    tempR = middleR;

    tempR.erase(1);

    if (tempL == ">")
    {
        tempL = "<";
        change = true;
    }
    else if (tempL == "\\")
    {
        tempL = "/";
        change = true;
    }


    if (tempR == "<")
    {
        tempR = ">";
        change = true;
    }
    else if (tempR == "/")
    {
        tempR = "\\";
        change = true;
    }

    if (change == true)
    {
        tempL += "|";

        middleR = tempL;
        middleL = tempR;

    }

    change = false;

    //Swap of Legs

    tempL = bottomL;
    tempR = bottomR;

    if (tempL == ">")
    {
        tempL = "<";
        change = true;
    }
    else if (tempL == "\\")
    {
        tempL = "/";
        change = true;
    }


    if (tempR == "<")
    {
        tempR = ">";
        change = true;
    }

    else if (tempR == "/")
    {
        tempR = "\\";
        change = true;
    }


    if (change == true)
    {
        bottomR = tempL;
        bottomL = tempR;

    }

}