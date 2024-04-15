"""
Streamlit app for visualizing behavior data
https://foraging-behavior-browser.streamlit.app/

Note the url is now queryable, e.g. https://foraging-behavior-browser.streamlit.app/?subject_id=41392

Example queries:
 /?subject_id=699982   # only show one subject
 /?session=10&session=20  # show sessions between 10 and 20
 /?tab_id=tab_1  # Show specific tab
 /?if_aggr_all=false

"""

#%%
import streamlit as st

def app():
    st.markdown('## Dear foraging browser user, \n'
                '#### For better stability and accessibility, this app has been migrated to Amazon ECS (thank you Yosef and Jon 🙌).\n'
                '#### 👉  [foraging-behavior-browser.allenneuraldynamics-test.org](http://foraging-behavior-browser.allenneuraldynamics-test.org/) '
                )
    st.markdown('#### If you see a window asking you to "Select a certificate", please click "Cancel".')
    st.divider()
    st.markdown('Ask Han or submit an issue [here](https://github.com/AllenNeuralDynamics/foraging-behavior-browser/issues) if you have any questions.')

app()

