{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "is_permutation_1=\"Top\"\n",
    "is_permutation_2=\"Pot\"\n",
    "\n",
    "is_not_permutation_1=\"Okay\"\n",
    "is_not_permutation_2=\"Cool\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_perm(str_1,str_2):\n",
    "    str_1=str_1.lower()\n",
    "    str_2=str_2.lower()\n",
    "    \n",
    "    if len(str_1)!=len(str_2):\n",
    "        return False\n",
    "    \n",
    "    str_1=''.join(sorted(str_1))\n",
    "    str_2=''.join(sorted(str_2))\n",
    "    \n",
    "    for i in range(len(str_1)):\n",
    "        if str_1[i]!=str_2[i]:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "print(is_perm(is_permutation_1,is_permutation_2))\n",
    "print(is_perm(is_not_permutation_1,is_not_permutation_2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
