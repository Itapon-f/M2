/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: itapon-f <itapon-f@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 14:26:01 by itapon-f          #+#    #+#             */
/*   Updated: 2025/12/29 14:52:59 by itapon-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


char	**ft_free(char **spl, int row)
{
	int		i;

	i = 0;
	while (i < row)
	{
		free(spl[i]);
		i++;
	}
	free (spl);
	return (0);
}

static int	ft_w_len(char const *s, char c)
{
	int	length;
	int	k;

	length = 0;
	k = 0;
	while (s[k] && s[k] == c)
		k++;
	while (s[k] && s[k] != c)
	{
		length++;
		k++;
	}
	return (length);
}

static char	*ft_split_copy(const char *s, int *i, char c)
{
	unsigned int	j;
	char			*copied;

	copied = ft_calloc((ft_w_len(s + *i, c) + 1), sizeof(char));
	if (!copied)
		return (NULL);
	j = 0;
	while (s[*i] == c)
		(*i)++;
	while (s[*i] && s[*i] != c)
	{
		while (s[*i] == c)
			(*i)++;
		copied[j] = s[*i];
		j++;
		(*i)++;
	}
	return (copied);
}

static int	ft_count_words(char const *s, char c)
{
	unsigned int	word;
	unsigned int	j;
	int				in_word;

	in_word = 0;
	word = 0;
	j = 0;
	while (s[j])
	{
		if (s[j] != c && !in_word)
		{
			word++;
			in_word = 1;
		}
		if (s[j] == c)
		{
			in_word = 0;
		}
		j++;
	}
	return (word);
}

char	**ft_split(char const *s, char c)
{
	char	**spl;
	int		i;
	int		row;
	int		words;

	row = 0;
	words = ft_count_words(s, c);
	spl = (char **)ft_calloc(words + 1, sizeof(char *));
	if (!spl)
		return (0);
	i = 0;
	while (row < words)
	{
		spl[row] = ft_split_copy(s, &i, c);
		if (!spl[row])
			return (ft_free(spl, row));
		row++;
	}
	return (spl);
}

void	ft_free_split(char **arr)
{
	int	i;

	i = 0;
	while(arr[i])
		free(arr[i++]);
	free(arr);
}