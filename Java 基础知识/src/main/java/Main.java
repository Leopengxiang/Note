public class Main {
    public static void main(String[] args) {

    }


    /**
     * 静态代理
     */
    public static void staticProxy() {
        Movie movie = new StarTrekMovie();
        movie = new TheaterMovieProxy(movie);
        movie.play();
    }
}
