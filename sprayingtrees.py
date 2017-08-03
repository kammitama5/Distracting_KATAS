def task(w,n,c):
    d = n * c
    if w == 'Monday':
        return 'It is {} today, James, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w, n, d)
    elif w == 'Tuesday':
        return 'It is {} today, John, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w, n, d)
    elif w == 'Wednesday':
        return 'It is {} today, Robert, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w, n, d)
    elif w == 'Thursday':
        return 'It is {} today, Michael, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w, n, d)
    elif w == 'Friday':
        return 'It is {} today, William, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w, n, d)
    