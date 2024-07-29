
import pandas as pd



# Define the data
data = [
    {
        'Riddle 1': "Transparent and delicate, I hold the elixir of celebration. What am I?",
        'Answer 1': "Wine glass",
        'Riddle 2': "I am a vessel, ready to be filled with savory delights. What am I?",
        'Answer 2': "Bowl",
        'Riddle 3': "Gathered around me, people savor meals and share stories. What am I?",
        'Answer 3': "Dining table",
        'Riddle 4': "With a sharp edge, I slice through food with ease. What am I?",
        'Answer 4': "Knife",
        'Riddle 5': "I am a sweet treat, baked to perfection. What am I?",
        'Answer 5': "Cake"
    },
    {
        'Riddle 1': "You drink from me, and I come in many shapes and sizes.",
        'Answer 1': "Cup",
        'Riddle 2': "A round, red temptation that keeps the doctor away?",
        'Answer 2': "Apple",
        'Riddle 3': "I hold liquid that quenches your thirst, but won't pour.",
        'Answer 3': "Bottle",
        'Riddle 4': "Layers of deliciousness between two slices of bread.",
        'Answer 4': "Sandwich",
        'Riddle 5': "I'm a color, citrus delight, peel my skin, taste the light. What am I?",
        'Answer 5': "Orange"
    },
    {
        'Riddle 1': "I support you when you need to rest, come take a seat. What am I?",
        'Answer 1': "Chair",
        'Riddle 2': "A figure among the lively crowd, part of the family. What am I?",
        'Answer 2': "Person",
        'Riddle 3': "A decorative vessel holding beauty within, can you find it? What am I?",
        'Answer 3': "Vase",
        'Riddle 4': "A loyal companion with a wagging tail, spot the furry friend. What am I?",
        'Answer 4': "Dog",
        'Riddle 5': "Nature's touch inside the house, spot the greenery.",
        'Answer 5': "Potted plant"
    }
]

# Create a Pandas DataFrame
rid_answrs = pd.DataFrame(data)

# Get the total number of rows in the DataFrame
total_rows = rid_answrs.shape[0]

# Calculate the start and end indices for the last chunk
start_index = 2 * (total_rows // 3)
end_index = total_rows

# Access the last chunk of rows
last_chunk = rid_answrs[start_index:end_index]

# Extract riddles and answers into variables
riddle1, riddle2, riddle3, riddle4, riddle5 = last_chunk['Riddle 1'].values[0], last_chunk['Riddle 2'].values[0], last_chunk['Riddle 3'].values[0], last_chunk['Riddle 4'].values[0], last_chunk['Riddle 5'].values[0]
answer1, answer2, answer3, answer4, answer5 = last_chunk['Answer 1'].values[0], last_chunk['Answer 2'].values[0], last_chunk['Answer 3'].values[0], last_chunk['Answer 4'].values[0], last_chunk['Answer 5'].values[0]



start_index = total_rows // 3
end_index = 2 * (total_rows // 3)
# Access the middle chunk of rows
middle_chunk = rid_answrs[start_index:end_index]

# Extract riddles and answers into variables for the middle chunk
riddle6, riddle7, riddle8, riddle9, riddle10 = middle_chunk['Riddle 1'].values[0], middle_chunk['Riddle 2'].values[0], middle_chunk['Riddle 3'].values[0], middle_chunk['Riddle 4'].values[0], middle_chunk['Riddle 5'].values[0]
answer6, answer7, answer8, answer9, answer10 = middle_chunk['Answer 1'].values[0], middle_chunk['Answer 2'].values[0], middle_chunk['Answer 3'].values[0], middle_chunk['Answer 4'].values[0], middle_chunk['Answer 5'].values[0]