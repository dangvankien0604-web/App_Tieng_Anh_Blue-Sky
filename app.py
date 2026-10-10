import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

const Flashcard = ({ word, meaning }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => setIsFlipped(!isFlipped)}
    >
      <Text style={styles.text}>
        {isFlipped ? meaning : word}
      </Text>
    </TouchableOpacity>
  );
};

const App = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Ôn Tập Tiếng Anh</Text>
      <Flashcard word="Vocabulary" meaning="Từ vựng" />
      <Flashcard word="Pronunciation" meaning="Phát âm" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#f0f4f8' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20, color: '#333' },
  card: { 
    width: 300, 
    height: 200, 
    backgroundColor: '#fff', 
    justifyContent: 'center', 
    alignItems: 'center', 
    borderRadius: 15, 
    shadowColor: '#000', 
    shadowOffset: { width: 0, height: 4 }, 
    shadowOpacity: 0.1, 
    elevation: 5, 
    marginBottom: 20 
  },
  text: { fontSize: 28, fontWeight: '600', color: '#2c3e50' }
});

export default App;
