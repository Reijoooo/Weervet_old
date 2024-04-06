import React from 'react';
import Header from '../react_components/Header';

const App = () => {
    return (
        <div>
            <Header />
            {<h1>Содержимое</h1>}
        </div>
    );
    // return (
    //     <Router>
    //         <Header />
    //         <Switch>
    //             <Route path="/" exact component={HomePage} />
    //             <Route path="/about" component={AboutPage} />
    //             <Route path="/contact" component={ContactPage} />
    //         </Switch>
    //         <Footer />
    //     </Router>
    // );
};

//ReactDOM.render(<App />, document.getElementById('root'));
export default App;