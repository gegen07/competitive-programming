#include <iostream>
#include <string>
#include <algorithm>
#include <iterator> 
#include <cstring>

using namespace std;
class Rochambo {

  public:
  int wins(string opponentGame) {

    string myGame = "RR";
    string rochambo = "RPS";

    string tmp;

    register size_t it;  

    for (it = 1; it < opponentGame.size(); ++it) {
      if (opponentGame[it] != opponentGame[it-1]) {
        tmp = rochambo;
        tmp.erase(tmp.find(opponentGame[it-1]), 1);
        tmp.erase(tmp.find(opponentGame[it]), 1);
        if (tmp.compare("R") == 0) {
          myGame.push_back('P');
        } else if (tmp.compare("S") == 0) {
          myGame.push_back('R');
        } else {
          myGame.push_back('S');
        }
        
      } else {
        if (opponentGame[it-1] == 'R') {
          myGame.push_back('P');
        } else if (opponentGame[it-1] == 'S') {
          myGame.push_back('R');
        } else {
          myGame.push_back('S');
        }
      }
    }

    int count = 0;

    for (it = 0; it != opponentGame.size(); ++it) {
      if ((opponentGame[it] == 'R' && myGame[it] == 'P') 
          || (opponentGame[it] == 'S' && myGame[it] == 'R') 
          || (opponentGame[it] == 'P' && myGame[it] == 'S' )) {
        count++;
      } 
    }

    return count;
  }
};


