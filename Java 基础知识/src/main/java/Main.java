public class Main {
    public static void main(String[] args) {

    }


    /**
     * ้ๆไปฃ็
     */
    public static void staticProxy() {
        Movie movie = new StarTrekMovie();
        movie = new TheaterMovieProxy(movie);
        movie.play();
    }
}
