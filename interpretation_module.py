import pandas as pd

def generate_interpretation(prediction_output):
    prediction = prediction_output['prediction']
    pred_prob = prediction_output['pred_prob']
    feature_importances = prediction_output['feature_importances']
    
    interpretation = ''
    if prediction == 0:
        interpretation = 'Customer will not churn'
        interpretation += '\nReason: Prediction Probability is {}'.format(pred_prob)
    else:
        interpretation = 'Customer will churn'
        interpretation += '\nReason: Prediction Probability is {}'.format(pred_prob)

    interpretation += 'Feature Importance:\n'
    for feature, importance in feature_importances:
        interpretation += '{}: {}\n'.format(feature, importance)

    return interpretation
