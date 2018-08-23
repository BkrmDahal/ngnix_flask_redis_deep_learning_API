Endpoints
=========

predict
-------

    Input:

        .. code-block:: bash

            curl -X POST -F image=@jemma.png 'http://localhost/predict'

    Output:

        .. code-block:: json

            {
            "predictions": [
                {
                "label": "beagle", 
                "probability": 0.9461532831192017
                }, 
                {
                "label": "bluetick", 
                "probability": 0.031958963721990585
                }, 
                {
                "label": "redbone", 
                "probability": 0.0066171870566904545
                }, 
                {
                "label": "Walker_hound", 
                "probability": 0.003387963864952326
                }, 
                {
                "label": "Greater_Swiss_Mountain_dog", 
                "probability": 0.0025766845792531967
                }
            ], 
            "success": true
            }