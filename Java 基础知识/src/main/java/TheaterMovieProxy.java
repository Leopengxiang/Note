public class TheaterMovieProxy implements Movie{
    private Movie proxyedObj;

    TheaterMovieProxy(Movie movie) {
        this.proxyedObj = movie;
    }

    @Override
    public void play() {
        System.out.println("openning ads is playing");
        proxyedObj.play();
        System.out.println("close ads is playing");
    }
}
