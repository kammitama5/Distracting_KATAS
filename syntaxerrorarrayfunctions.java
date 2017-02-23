import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

/**
 * Created by Javatlacati on 22/02/2017.
 */
public class Foo {
    public static List<Function<String, Integer>> arrOfFuncs = new ArrayList<>();

    static {
        arrOfFuncs.add((num) -> Integer.parseInt(num, 2));
        arrOfFuncs.add((num) -> Integer.parseInt(num, 8));
    }

    public Integer convert(String num, int base) {
        return arrOfFuncs.get(base).apply(num);
    }

}

