#include <cstring>
#include <cctype>

std::string capital (std::string name )
{
  name[0] = toupper(name[0]);
  return name;
}

